import pandas
import json

excel_data = pandas.read_excel(io="sbt_certificate_issuance_list.xlsx",
                               header=2,
                               nrows=43)

json_data = json.loads(excel_data.to_json(orient="index"))

#Writing into file
with open("sample.json", "w") as file:
    file.write(json.dumps(json_data, indent=4))


