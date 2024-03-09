from cergen import *
import numpy as np
import math


create_nested_list_durations = []
create_nested_list_with_fill_durations = []
get_transpose_of_nested_list_durations = []
get_shape_of_nested_list_durations = []
unnest_list_durations = []
nest_list_durations = []
map_nested_list_durations = []


def test_create_nested_list():
    # random dimension
    dimension = random.randint(0,10)

    # random boyut
    shape = tuple([random.randint(1, 10) for _ in range(dimension)]) if dimension != 0 else ()

    print("testing create_nested_list with shape", shape, flush=True)

    start = time.time()

    # nested list
    nested_list = create_nested_list(shape, (1, 10), True)

    end = time.time()

    print("create_nested_list with shape", shape, "took", end-start, "seconds")

    create_nested_list_durations.append(end-start)


def test_create_nested_list_with_fill():
    # random dimension
    dimension = random.randint(0, 10)

    # random boyut
    shape = tuple([random.randint(1, 10) for _ in range(dimension)]) if dimension != 0 else ()

    # fill value
    fill = random.random()

    print("testing create_nested_list_with_fill with shape", shape, "and fill", fill, flush=True)

    start = time.time()

    # nested list
    nested_list = create_nested_list_with_fill(shape, 0, fill)

    end = time.time()

    print("create_nested_list_with_fill with shape", shape, "took", end-start, "seconds")

    create_nested_list_with_fill_durations.append(end-start)


def test_get_transpose_of_nested_list():
    # random dimension
    dimension = random.randint(0, 10)

    # random boyut
    shape = tuple([random.randint(1, 10) for _ in range(dimension)]) if dimension != 0 else ()

    print("testing get_transpose_of_nested_list with shape", shape, flush=True)

    # nested list
    nested_list = create_nested_list(shape, (1, 10), True)

    start = time.time()

    # transpose
    transposed = get_transpose_of_nested_list(nested_list)

    end = time.time()

    print("get_transpose_of_nested_list with shape", shape, "took", end-start, "seconds")


def test_get_shape_of_nested_list():
    # random dimension
    dimension = random.randint(0, 10)

    # random boyut
    shape = tuple([random.randint(1, 10) for _ in range(dimension)]) if dimension != 0 else ()

    print("testing get_shape_of_nested_list with shape", shape, flush=True)

    # nested list
    nested_list = create_nested_list(shape, (1, 10), True)

    start = time.time()

    # shape
    actual = get_dimensions_of_nested_list(nested_list)

    end = time.time()

    print("get_shape_of_nested_list with shape", shape, "took", end-start, "seconds")


def test_unnest_list():
    # random dimension
    dimension = random.randint(0, 10)

    # random boyut
    shape = tuple([random.randint(1, 10) for _ in range(dimension)]) if dimension != 0 else ()

    print("testing unnest_list with shape", shape, flush=True)

    nested_list = create_nested_list(shape, (1, 10), True)

    start = time.time()

    # unnest
    actual = unnest_list(nested_list)

    end = time.time()

    print("unnest_list with shape", shape, "took", end-start, "seconds")

    unnest_list_durations.append(end-start)


def test_nest_list():
    # random dimension
    dimension = random.randint(0, 10)

    # random boyut
    shape = tuple([random.randint(1, 10) for _ in range(dimension)]) if dimension != 0 else ()

    # unnested list
    unnested_list = [random.random() for _ in range(np.prod(shape))] if dimension != 0 else [random.random()]

    print("testing nest_list with shape", shape, flush=True)

    start = time.time()

    # nested list
    actual = nest_list(unnested_list, shape)

    end = time.time()

    print("nest_list with shape", shape, "took", end-start, "seconds")

    nest_list_durations.append(end-start)


def test_map_nested_list():
    # random dimension
    dimension = random.randint(0, 10)

    # random boyut
    shape = tuple([random.randint(1, 10) for _ in range(dimension)]) if dimension != 0 else ()

    print("testing map_nested_list with shape", shape, flush=True)

    # nested list
    nested_list = create_nested_list(shape, (1, 10), True)
    """
secose
    """

    start = time.time()

    # map
    actual = map_nested_list(nested_list, lambda x: x + x**2 - 3 / x)

    end = time.time()

    print("map_nested_list with shape", shape, "took", end-start, "seconds")

    map_nested_list_durations.append(end-start)


def main():
    for _ in range(100):
        test_create_nested_list()
        test_create_nested_list_with_fill()
        test_get_transpose_of_nested_list()
        test_get_shape_of_nested_list()
        test_unnest_list()
        test_nest_list()
        test_map_nested_list()


if __name__ == "__main__":
    main()
    print("create_nested_list durations:", create_nested_list_durations, "average:", sum(create_nested_list_durations)/len(create_nested_list_durations))
    print("create_nested_list_with_fill durations:", create_nested_list_with_fill_durations, "average:", sum(create_nested_list_with_fill_durations)/len(create_nested_list_with_fill_durations))
    print("get_transpose_of_nested_list durations:", get_transpose_of_nested_list_durations, "average:", sum(get_transpose_of_nested_list_durations)/len(get_transpose_of_nested_list_durations))
    print("get_shape_of_nested_list durations:", get_shape_of_nested_list_durations, "average:", sum(get_shape_of_nested_list_durations)/len(get_shape_of_nested_list_durations))
    print("unnest_list durations:", unnest_list_durations, "average:", sum(unnest_list_durations)/len(unnest_list_durations))
    print("nest_list durations:", nest_list_durations, "average:", sum(nest_list_durations)/len(nest_list_durations))
    print("map_nested_list durations:", map_nested_list_durations, "average:", sum(map_nested_list_durations)/len(map_nested_list_durations))

