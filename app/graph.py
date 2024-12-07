from altair import Chart


def chart(df, x, y, target) -> Chart:

    '''Creates an interactive scatter plot visualization using Altair.'''

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
        padding={"left": 6, "right": 6, "top": 8, "bottom": 8}
    ).configure(
        title={"fontSize": 20, "font": "Helvetica"}
    ).configure_axis(
        gridColor="lightgray",
        gridOpacity=0.2
    ).configure_view(
        stroke="lightgray",
        strokeWidth=2
    ).interactive()

    return graph

