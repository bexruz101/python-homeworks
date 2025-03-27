from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")

table = soup.find("table")

days = []
temperatures = []
conditions = []

for row in table.find_all("tr")[1:]:
    day, temp, condition = [cell.get_text(strip=True) for cell in row.find_all("td")]
    days.append(day)
    temperatures.append(temp.replace("°C", "").strip())
    conditions.append(condition)


print("Weather Forecast:")
print("Day\tTemperature\tCondition")
for day, temp, condition in zip(days, temperatures, conditions):
    print(f"{day}\t{temp}°C\t\t{condition}")


try:
    temperature_values = [int(temp) for temp in temperatures]
except ValueError as e:
    print(f"Error converting temperatures: {e}")
    exit()


max_temp = max(temperature_values)
max_temp_day = days[temperature_values.index(max_temp)]
print(f"\nDay with highest temperature: {max_temp_day} ({max_temp}°C)")


sunny_days = [day for day, cond in zip(days, conditions) if cond.lower() == "sunny"]
print(f"Days with 'Sunny' condition: {', '.join(sunny_days)}")


avg_temperature = sum(temperature_values) / len(temperature_values)
print(f"\nAverage temperature for the week: {avg_temperature:.2f}°C")
