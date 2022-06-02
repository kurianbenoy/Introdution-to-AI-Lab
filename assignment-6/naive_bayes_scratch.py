from sklearn.datasets import load_iris
from math import sqrt, pi, exp


# def separate_by_class(X, y):
#     separted_dict = {}
#     for i in range(len(X)):
#         print(X[i])
#         print(type(y[i]))
#         if y[i] not in separted_dict:
#             separted_dict[y[i]] = []
#         separted_dict[int(y[i])].append(X[i])
#     return separted_dict


def separate_by_class(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        class_value = vector[-1]
        if class_value not in separated:
            separated[class_value] = []
        separated[class_value].append(vector)
    return separated


def mean(numbers):
    return sum(numbers) / float(len(numbers))


def stddev(numbers):
    avg = mean(numbers)
    variance = sum([(x - avg) ** 2 for x in numbers]) / float(len(numbers) - 1)
    return sqrt(variance)


def summarize_dataset(dataset):
    summaries = [
        (mean(column), stddev(column), len(column)) for column in zip(*dataset)
    ]
    del summaries[-1]
    return summaries


def summarize_by_class(dataset):
    separated = separate_by_class(dataset)
    summaries = dict()
    for class_value, rows in separated.items():
        summaries[class_value] = summarize_dataset(rows)
    return summaries


def calculate_probability(x, mean, stddev):
    exponent = exp(-((x - mean) ** 2 / (2 * stddev ** 2)))
    return (1 / (sqrt(2 * pi) * stddev)) * exponent


def calculate_class_probability(summaries, row):
    total_rows = sum([summaries[label][0][2] for label in summaries])
    probabilities = dict()

    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = summaries[class_value][0][2] / float(total_rows)
        for i in range(len(class_summaries)):
            mean, stdev, count = class_summaries[i]
            probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
    return probabilities


if __name__ == "__main__":
    dataset = [
        [3.393533211, 2.331273381, 0],
        [3.110073483, 1.781539638, 0],
        [1.343808831, 3.368360954, 0],
        [3.582294042, 4.67917911, 0],
        [2.280362439, 2.866990263, 0],
        [7.423436942, 4.696522875, 1],
        [5.745051997, 3.533989803, 1],
        [9.172168622, 2.511101045, 1],
        [7.792783481, 3.424088941, 1],
        [7.939820817, 0.791637231, 1],
    ]

    summary = summarize_by_class(dataset)
    for label in summary:
        print(label)
        for row in summary[label]:
            print(row)

    print(calculate_probability(1.0, 1.0, 1.0))
    print(calculate_probability(2.0, 1.0, 1.0))
    print(calculate_probability(0.0, 1.0, 1.0))

    probabilities = calculate_class_probability(summary, dataset[0])
    print(probabilities)
