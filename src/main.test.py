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

    random_int_or_none_arg = None
    random_int_arg = random.randint(1, 10)
    
    if len(boyut) > 1:
        random_int_or_none_arg = random.randint(0, len(boyut) - 1)

    methods_and_np_equivalents = [
        # (method, np_equivalent, takes_argument, argument_type)
        (veri1.us, np.power, True, int),
        (veri1.topla, np.sum, True, int),
        (veri1.ortalama, np.average, True, int),
    ]

    random_method, random_np_equivalent, _, _ = random.choice(methods_and_np_equivalents)

    start = time.time()

    calculated = random_method(random_int_arg if random_method.__name__ == "us" else random_int_or_none_arg)

    end = time.time()

    start_np = time.time()

    actual = random_np_equivalent(np_arr1, random_int_arg if random_method.__name__ == "us" else random_int_or_none_arg)

    end_np = time.time()

    test_results = TestResult(
        durations=(end-start, end_np-start_np),
        results=(calculated if isinstance(calculated, (int, float)) else calculated.listeye(), actual),
        test_name="total_random_example " + random_method.__name__ + " with shape " + str(boyut)
    )

    print(test_results)

    return test_results


def total_random_example_gergo_arg():
    # random dimension
    dimension = random.randint(1, 2)

    # random boyut
    boyut_list = [random.randint(1, 6) for _ in range(dimension)]
    reversed_boyut_list = boyut_list[::-1]
    
    boyut = tuple(boyut_list)

    veri1 = rastgele_gercek(boyut)
    veri2 = rastgele_gercek(boyut).devrik()

    np_arr1 = np.array(veri1.listeye())
    np_arr2 = np.array(veri2.listeye())
    np_arr3 = np.array(veri2.devrik().listeye())

    methods_and_np_equivalents = [
        # (method, np_equivalent, takes_argument, argument_type)
        (veri1.ic_carpim, np.inner, False, None),
        (veri1.dis_carpim, np.outer, False, None),
    ]

    if len(boyut) == 2:
        random_method, random_np_equivalent, _, _ = methods_and_np_equivalents[0]
    else:
        random_method, random_np_equivalent, _, _ = methods_and_np_equivalents[1]

    start = time.time()

    calculated = random_method(veri2)

    end = time.time()

    start_np = time.time()

    actual = random_np_equivalent(np_arr1, np_arr2 if len(boyut) == 1 else np_arr3)

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

    tests_per_run = 9
        
    for i in range(total_tests):
        results.append(example_1().to_obj())
        results.append(example_2().to_obj())
        results.append(example_3().to_obj())

        results.append(example_1().to_obj())
        results.append(example_2().to_obj())
        results.append(example_3().to_obj())
        
        results.append(total_random_example_no_arg().to_obj())
        results.append(total_random_example_gergo_arg().to_obj())
        results.append(total_random_example_int_arg().to_obj())
       

    total_times = [[], []]
    total_passed = 0

    failed_cases = []

    for i in range(total_tests * tests_per_run):
        total_times[0].append(results[i]["durations"][0])
        total_times[1].append(results[i]["durations"][1])

        if not results[i]["passed"]:
            failed_cases.append(str(results[i]["results"]))
            failed_cases.append(str(results[i]))
            print("Test failed: ", results[i]["test_name"])

        else:
            total_passed += 1

    print("Average time difference: ", np.mean(np.array(total_times[0]) - np.array(total_times[1])))
    print("Average time comparison: ", np.mean(np.array(total_times[0]) / np.array(total_times[1])))
    print("Success: ", total_passed * 100 / (total_tests * tests_per_run), "%")

    if len(failed_cases) > 0:
        print("Failed cases: ", len(failed_cases))
        print("Writing failed cases to file")

        with open("failed_cases.txt", "a") as f:
            for case in failed_cases:
                f.write(case + "\n")


if __name__ == "__main__":
    test()
