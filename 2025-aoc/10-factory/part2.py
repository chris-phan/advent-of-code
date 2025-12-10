from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

if __name__ == "__main__":
    f = open("input.txt", "r")

    joltages: list[list[int]] = []
    buttons: list[list[list[int]]] = []
    num_lights: list[int] = []

    for line in f:
        line_items = line.strip().split(" ")

        num_lights.append(len(line_items[0][1:-1]))

        buttons.append([])
        for button in line_items[1:-1]:
            button_nums = button[1:-1].split(",")
            int_buttons: list[int] = []
            for i in range(len(button_nums)):
                int_buttons.append(int(button_nums[i]))
            buttons[-1].append(int_buttons)

        joltages.append([])
        for jolts in line_items[-1][1:-1].split(","):
            joltages[-1].append(int(jolts))

    res = 0
    for i in range(len(buttons)):
        c = np.ones(len(buttons[i]))

        A: list[list[int]] = []
        for j in range(len(buttons[i])):
            A.append([0] * num_lights[i])
            for k in range(len(buttons[i][j])):
                A[-1][buttons[i][j][k]] = 1
        A_mat = np.array(A)
        b = np.array(joltages[i])
        constraint = LinearConstraint(A_mat.T, b, b)
        bounds = Bounds(lb=0, ub=np.inf)
        ans = milp(c, constraints=[constraint], bounds=bounds, integrality=np.ones(len(buttons[i])))
        res += sum(ans.x)

    print(f"res: {int(res)}")

