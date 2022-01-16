from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file("./graphs/simple_graph.html")
    fig = figure()

    num_values = int(input("Number of Values to Graph:  "))
    x_values = list(range(num_values))
    y_values = []

    with open("./graphs/number_data.txt", "r") as file:
        for line in file:
            y_values.append(line)

    fig.line(x_values, y_values, line_width=2)

    show(fig)