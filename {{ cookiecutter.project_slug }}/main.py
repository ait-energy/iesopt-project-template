import iesopt


model = iesopt.run("opt/config.iesopt.yaml")

df = model.results.to_pandas()

