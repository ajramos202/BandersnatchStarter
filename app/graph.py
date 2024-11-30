import pandas as pd
from altair import Chart

# data = {
#     "Category": ["A", "B", "C", "A", "B", "C"],
#     "Value1": [10, 20, 30, 15, 25, 35],
#     "Value2": [5, 15, 25, 10, 20, 30],
# }
# df = pd.DataFrame(data)


def chart(df, x, y, target) -> Chart:
    if x not in df.columns or y not in df.columns or target not in df.columns:
        raise ValueError("x, y, or target is not a valid column in the DataFrame.")

    graph = Chart(
        df,
        title=f"{y} by {x} for {target}",
    ).mark_circle(size=100).encode(
        x=x,
        y=y,
        color=target,
        tooltip=[f"{x}", f"{y}", f"{target}"]
    ).properties(
        width=600,
        height=400,
        background="#2d2d2d",
        padding={"left": 10, "right": 10, "top": 10, "bottom": 10}
    ).configure(
        title={"fontSize": 20, "font": "Helvetica"}
    ).interactive()
    return graph


if __name__ == "__main__":
    # Code to execute when you run `python graph.py`
    print("Running graph.py")


# Create chart
# my_chart = chart(df, x="Value1", y="Value2", target="Category")

# # Save the chart as an HTML file
# my_chart.save("chart_output.html")

# # Open the chart in your browser
# import webbrowser
# webbrowser.open("chart_output.html")

