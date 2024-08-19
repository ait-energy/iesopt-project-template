import iesopt


# Parse, build, and solve the model.
model = iesopt.run("opt/config.iesopt.yaml")

# Get the results as a pandas DataFrame.
df = model.results.to_pandas()

# Print the first 5 rows of a sub-part of the DataFrame.
print(df[df["field"] == "value"].head(5))
