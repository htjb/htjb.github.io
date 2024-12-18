import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta


def convert_to_date(date):
    if isinstance(date, str):
        try:
            return datetime.strptime(date, "%Y-%m-%d %H:%M:%S.%f").timestamp()
        except ValueError:
            return datetime.strptime(date, "%Y-%m-%d %H:%M:%S").timestamp()
    else:
        return np.nan


def diffs(t1, t2):
    if t1 is not np.NaN and t2 is not np.NaN:
        # If both times are valid, calculate the difference
        return t1 - t2
    else:
        # If any time is None (NaN), append None as the difference
        return np.NaN


def supo_style(supo):
    if supo == "Cosupervision":
        return "//"
    else:
        return ""


students = pd.read_excel("supervision.xlsx", dtype="str")
print(students)

supervision_style = students["Supervision Style"].values

y = np.arange(len(students["Name"]))

summer_s = [
    convert_to_date(students["Summer Start"].values[i])
    for i in range(len(students["Summer Start"]))
]
partIII_s = [
    convert_to_date(students["PartIII Start"].values[i])
    for i in range(len(students["PartIII Start"]))
]
Mphil_s = [
    convert_to_date(students["Mphil Start"].values[i])
    for i in range(len(students["Mphil Start"]))
]
PhD_s = [
    convert_to_date(students["PhD Start"].values[i])
    for i in range(len(students["PhD Start"]))
]

summer_e = [
    convert_to_date(students["Summer End"].values[i])
    for i in range(len(students["Summer End"]))
]
partIII_e = [
    convert_to_date(students["PartIII End"].values[i])
    for i in range(len(students["PartIII End"]))
]
Mphil_e = [
    convert_to_date(students["Mphil End"].values[i])
    for i in range(len(students["Mphil End"]))
]
PhD_e = [
    convert_to_date(students["PhD End"].values[i])
    for i in range(len(students["PhD End"]))
]

print(summer_s)
summer_diffs = np.array([diffs(summer_e[i], summer_s[i])
                         for i in range(len(summer_s))])
partIII_diffs = np.array(
    [diffs(partIII_e[i], partIII_s[i]) for i in range(len(partIII_s))]
)
Mphil_diffs = np.array([diffs(Mphil_e[i], Mphil_s[i])
                        for i in range(len(Mphil_s))])
PhD_diffs = np.array([diffs(PhD_e[i], PhD_s[i])
                      for i in range(len(PhD_s))])

hatch = [supo_style(supo) for supo in supervision_style]

# Convert the x-axis from seconds to months from October 2023
start_date = datetime(2023, 10, 1).timestamp()


# Function to convert seconds to months
def seconds_to_months(seconds):
    return seconds / (30 * 24 * 3600)


# Adjust the start times and durations to be in months from October 2023
summer_s = [seconds_to_months(s) for s in summer_s]
partIII_s = [seconds_to_months(s) for s in partIII_s]
Mphil_s = [seconds_to_months(s) for s in Mphil_s]
PhD_s = [seconds_to_months(s) for s in PhD_s]

summer_diffs = seconds_to_months(summer_diffs)
partIII_diffs = seconds_to_months(partIII_diffs)
Mphil_diffs = seconds_to_months(Mphil_diffs)
PhD_diffs = seconds_to_months(PhD_diffs)

fig, ax = plt.subplots()
plt.grid(zorder=1)
plt.barh(
    y=y,
    width=summer_diffs,
    left=summer_s,
    color="r",
    label="Summer",
    hatch=hatch,
    zorder=2,
)
plt.barh(
    y=y,
    width=partIII_diffs,
    left=partIII_s,
    color="g",
    label="Part III",
    hatch=hatch,
    zorder=2,
)
plt.barh(
    y=y,
    width=Mphil_diffs,
    left=Mphil_s,
    color="b",
    label="Mphil",
    hatch=hatch,
    zorder=2,
)
plt.barh(
    y=y, width=PhD_diffs, left=PhD_s, color="y", 
    label="PhD", hatch=hatch, zorder=2
)

minimum = []
for i in range(len(students["Name"])):
    minimum.append(np.nanmin([summer_s[i], 
                    partIII_s[i], Mphil_s[i], PhD_s[i]]))
    plt.text(minimum[i]-0.2, i, students["Name"].values[i], 
             ha='right', va='center', fontsize=10,
             bbox=dict(facecolor='white', edgecolor='white',
                        boxstyle='round,pad=0.2'))

plt.xticks(
    ax.get_xticks(),
    [
        datetime.fromtimestamp(30 * 24 * 3600 * x).strftime("%b %Y")
        for x in ax.get_xticks()
    ],
    rotation=45,
)

ax.set_xlim(left=seconds_to_months(start_date))


plt.gca().yaxis.set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

plt.legend()

plt.tight_layout()

plt.savefig("assets/supervisions.png", dpi=300, bbox_inches="tight")
plt.show()
