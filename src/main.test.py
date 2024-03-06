from cergen import *
import numpy as np
import math


def total_random_example_no_arg():
    # random dimension
    dimension = random.randint(0, 6)

    # random boyut
    boyut = tuple([random.randint(1, 10) for _ in range(dimension)]) if dimension != 0 else ()

    veri1 = rastgele_gercek(boyut)
    veri2 = rastgele_gercek(boyut)

    np_arr1 = np.array(veri1.listeye())
    np_arr2 = np.array(veri2.listeye())

    methods_and_np_equivalents = [
        # (method, np_equivalent, takes_argument, argument_type)
        (veri1.sin, np.sin, False, None),
        (veri1.cos, np.cos, False, None),
        (veri1.log, np.log10, False, None),
        (veri1.ln, np.log, False, None),
    ]

    random_method, random_np_equivalent, _, _ = random.choice(methods_and_np_equivalents)

    start = time.time()

    calculated = random_method()

    end = time.time()

    start_np = time.time()

    actual = random_np_equivalent(np_arr1)

    end_np = time.time()

    test_results = TestResult(
        durations=(end-start, end_np-start_np),
        results=(calculated if random_method.__name__ in ["L1", "L2"] else calculated.listeye(), actual),
        test_name="total_random_example " + random_method.__name__ + " with shape " + str(boyut)
    )

    print(test_results)

    return test_results


def total_random_example_int_arg():
    # random dimension
    dimension = random.randint(0, 5)

    # random boyut
    boyut = tuple([random.randint(1, 6) for _ in range(dimension)]) if dimension != 0 else ()

    veri1 = rastgele_gercek(boyut)

    np_arr1 = np.array(veri1.listeye())

    random_int_arg = random.randint(0, len(boyut) - 1)

    methods_and_np_equivalents = [
        # (method, np_equivalent, takes_argument, argument_type)
        (veri1.us, np.power, True, int),
        (veri1.topla, np.sum, True, int),
        (veri1.ortalama, np.average, True, int),
    ]

    random_method, random_np_equivalent, _, _ = random.choice(methods_and_np_equivalents)

    start = time.time()

    calculated = random_method(random_int_arg)

    end = time.time()

    start_np = time.time()

    actual = random_np_equivalent(np_arr1, random_int_arg)

    end_np = time.time()

    test_results = TestResult(
        durations=(end-start, end_np-start_np),
        results=(calculated if isinstance(calculated, (int, float)) else calculated.listeye(), actual),
        test_name="total_random_example " + random_method.__name__ + " with shape " + str(boyut)
    )

    print(test_results)

    return test_results


def test():
    results = []

    total_tests = 100
        
    for i in range(total_tests):
        results.append(example_1().to_obj())
        results.append(example_2().to_obj())
        results.append(example_3().to_obj())

        results.append(example_1().to_obj())
        results.append(example_2().to_obj())
        results.append(example_3().to_obj())
        """
        results.append(total_random_example_no_arg().to_obj())
        results.append(total_random_example_no_arg().to_obj())
        results.append(total_random_example_int_arg().to_obj())
        """

    total_time_diff = 0
    total_passed = 0

    failed_cases = []

    for i in range(total_tests * 6):
        total_time_diff += results[i]["durations"][0] - results[i]["durations"][1]

        if not results[i]["passed"]:
            failed_cases.append(results[i]["results"])
            print("Test failed: ", results[i]["test_name"])

        else:
            total_passed += 1

    print("Average time difference: ", total_time_diff / (total_tests * 6))
    print("Success: ", total_passed * 100 / (total_tests * 6) + "%")

    if len(failed_cases) > 0:
        print("Failed cases: ", len(failed_cases))
        print("Writing failed cases to file")

        with open("failed_cases.txt", "a") as f:
            for case in failed_cases:
                f.write(str(case)[0] + "\n" + str(case)[1] + "\n\n\n")


if __name__ == "__main__":
    test()
