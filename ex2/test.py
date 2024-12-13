from data_summary import DataSummary


def run_test(test_name, func, args, expected):
    try:
        result = func(*args)
        if result != expected:
            print(f"{test_name}: Failure (Expected: {expected}, Got: {result})")
    except Exception as err:
        if err.args[0] != str(expected):
            print(f"{test_name}: Failure (Expected: {expected}, Got: {err})")


if __name__ == "__main__":
    run_test(
        "DS_err",
        DataSummary,
        [],
        "Data file and meta file must be provided",
    )
    run_test(
        "DS_err",
        DataSummary,
        ["happiness.json"],
        "Data file and meta file must be provided",
    )
    run_test(
        "DS_err",
        DataSummary,
        [None, "happiness_meta.csv"],
        "Data file and meta file must be provided",
    )

    DS = DataSummary(datafile="happiness.json", metafile="happiness_meta.csv")
    run_test(
        "Test DS[3]",
        DS.__getitem__,
        [3],
        {
            "Country": "Norway",
            "Region": "Western Europe",
            "Happiness Rank": "4",
            "Happiness Score": "7.522",
            "Standard Error": "0.0388",
            "Economy": "1.459",
            "Family": "1.33095",
            "Class": "A",
        },
    )
    run_test(
        "Test DS['Country']",
        DS.__getitem__,
        ["Country"],
        [row["Country"] for row in DS.data if "Country" in row],
    )
    run_test(
        "Test DS['GDP']", DS.__getitem__, ["GDP"], "Feature 'GDP' not found in data"
    )
    run_test(
        "Test DS['data']",
        DS.__getitem__,
        ["data"],
        "Feature 'data' not found in data",
    )
    run_test(
        "Test DS.mean('Happiness Score')",
        DS.mean,
        ["Happiness Score"],
        sum(
            float(row["Happiness Score"])
            for row in DS.data
            if row["Happiness Score"] is not None
        )
        / sum(1 for row in DS.data if row["Happiness Score"] is not None),
    )
    run_test(
        "Test DS.mode('Class')",
        DS.mode,
        ["Class"],
        ["K", "H", "N", "B", "L", "A", "M", "D", "G", "C"],
    )
    run_test("Test DS.unique('Region')", DS.unique, ["Region"], [])
    run_test(
        "Test DS.unique('Country')",
        DS.unique,
        ["Country"],
        sorted(set(row["Country"] for row in DS.data if row["Country"] is not None)),
    )

    run_test(
        "Test DS.sum('Economy')",
        DS.sum,
        ["Economy"],
        sum(float(row["Economy"]) for row in DS.data if row["Economy"] is not None),
    )
    run_test(
        "Test DS.count('Country')",
        DS.count,
        ["Country"],
        sum(1 for row in DS.data if row["Country"] is not None),
    )
    run_test(
        "Test DS.max('Economy')",
        DS.max,
        ["Economy"],
        max(float(row["Economy"]) for row in DS.data if row["Economy"] is not None),
    )
    run_test(
        "Test DS.empty('Standard Error')",
        DS.empty,
        ["Standard Error"],
        sum(row["Standard Error"] is None for row in DS.data),
    )

    # Additional tests
    run_test(
        "Test DS.sum('Family')",
        DS.sum,
        ["Family"],
        sum(float(row["Family"]) for row in DS.data if row["Family"] is not None),
    )
    run_test(
        "Test DS.count('Happiness Rank')",
        DS.count,
        ["Happiness Rank"],
        sum(1 for row in DS.data if row["Happiness Rank"] is not None),
    )
    run_test(
        "Test DS.mean('Standard Error')",
        DS.mean,
        ["Standard Error"],
        sum(
            float(row["Standard Error"])
            for row in DS.data
            if row["Standard Error"] is not None
        )
        / sum(1 for row in DS.data if row["Standard Error"] is not None),
    )
    run_test(
        "Test DS.min('Economy')",
        DS.min,
        ["Economy"],
        min(float(row["Economy"]) for row in DS.data if row["Economy"] is not None),
    )
    run_test(
        "Test DS.max('Happiness Score')",
        DS.max,
        ["Happiness Score"],
        max(
            float(row["Happiness Score"])
            for row in DS.data
            if row["Happiness Score"] is not None
        ),
    )
    run_test(
        "Test DS.unique('Class')",
        DS.unique,
        ["Class"],
        [],
    )
    run_test(
        "Test DS.mode('Region')",
        DS.mode,
        ["Region"],
        [
            "Sub-Saharan Africa",
            "Central and Eastern Europe",
            "Latin America and Caribbean",
            "Western Europe",
            "Middle East and Northern Africa",
            "Southeastern Asia",
            "Southern Asia",
            "Eastern Asia",
            "North America",
            "Australia and New Zealand",
        ],
    )
    run_test(
        "Test DS.empty('GDP')",
        DS.empty,
        ["GDP"],
        expected="Feature 'GDP' not found in data",
    )

    DS.to_csv("happiness.csv")  # Expected: CSV file creation
    print("CSV file creation: Success")
