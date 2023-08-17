import PySimpleGUI as sg

layout = [
    [
        sg.Input(key="-INPUT-"),
        [
            sg.Spin(
                [
                    "km to mile",
                    "mile to km",
                    "kg to pound",
                    "pound to kg",
                    "celcius to Fahrenheit",
                    "Fahrenheit to celcius",
                ],
                key="-UNITS-",
            )
        ],
        sg.Button("Convert", key="-CONVERT-"),
    ],
    [sg.Text("Result", key="-RESULT-"), sg.Button("Clear", key="-CLEAR-")],
]


window = sg.Window("converter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-CONVERT-":
        input_value = values["-INPUT-"]

        if input_value.isnumeric():
            print(input_value)

            match values["-UNITS-"]:
                case "km to mile":
                    output_value = round(float(input_value) * 0.6214, 2)
                    output = f"{input_value} km is {output_value} miles."

                case "mile to km":
                    output_value = round(float(input_value) * 1.6093, 2)
                    output = f"{input_value} miles is {output_value} km."

                case "kg to pound":
                    output_value = round(float(input_value) * 2.2046, 2)
                    output = f"{input_value} kg is {output_value} pound."

                case "pound to kg":
                    output_value = round(float(input_value) * 0.4536, 2)
                    output = f"{input_value} pound is {output_value} kg."

                case "celcius to Fahrenheit":
                    output_value = round(float(input_value) * 32, 2)
                    output = f"{input_value} celcuis is {output_value} Fahrenheit."

                case "Fahrenheit to celcius":
                    output_value = round(float(input_value) * -17.7778, 2)
                    output = f"{input_value} fahrenheit is {output_value} celcius."

            window["-RESULT-"].update(output)
        else:
            window["-RESULT-"].update("enter a numeric value")

    if event == "-CLEAR-":
        window["-RESULT-"].update("Result")
        window["-INPUT-"].update("")

window.close()
