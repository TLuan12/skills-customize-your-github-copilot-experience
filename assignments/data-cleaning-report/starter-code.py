import csv


def load_data(file_path):
    with open(file_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
    return rows


def clean_data(rows):
    # TODO: handle missing values, normalize text, and remove duplicates
    return rows


def summarize_data(rows):
    # TODO: compute summary statistics and counts
    return {}


if __name__ == "__main__":
    data = load_data("data.csv")
    cleaned = clean_data(data)
    summary = summarize_data(cleaned)
    print("Cleaned data:", cleaned)
    print("Summary:", summary)
