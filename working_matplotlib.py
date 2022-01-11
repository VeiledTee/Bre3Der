import matplotlib

matplotlib.use("TkAgg")
import os
import random
from copy import deepcopy
from typing import List

import matplotlib.pyplot as plt
import mpl_toolkits
import numpy as np
import stl
from mpl_toolkits import mplot3d
from numpy import ndarray

NUM_GEN: int = 10
C_RATE: float = 0.8
M_RATE: float = 1
T_RATE: float = 1
POP_SIZE: int = 10
POPULATION: List[ndarray] = []
CURRENT_DIRECTORY: str = ""
CURRENT_USER: str = ""


def plot_population() -> None:
    fig = plt.figure(figsize=plt.figaspect(0.5))
    for i in range(POP_SIZE):
        my_mesh = stl.mesh.Mesh(POPULATION[i].copy())
        ax = fig.add_subplot(2, 5, i + 1, projection="3d")
        ax.add_collection3d(mpl_toolkits.mplot3d.art3d.Poly3DCollection(my_mesh.vectors))
        scale = my_mesh.points.flatten()
        ax.auto_scale_xyz(scale, scale, scale)
    plt.show()


def save_and_plot(to_plot, save_file: str, show_plot: bool = False):
    my_mesh = stl.mesh.Mesh(to_plot.copy())
    my_mesh.save(f"{save_file}.stl", mode=stl.Mode.BINARY)
    if show_plot:
        figure = plt.figure()
        axes = mpl_toolkits.mplot3d.Axes3D(figure)
        axes.add_collection3d(mpl_toolkits.mplot3d.art3d.Poly3DCollection(my_mesh.vectors))
        scale = my_mesh.points.flatten()
        axes.auto_scale_xyz(scale, scale, scale)
        plt.show()


def make_cube() -> ndarray:
    data = np.zeros(12, dtype=stl.mesh.Mesh.dtype)
    # Looks like everything is defined as a triangle
    # Top face
    # (x -- left right, y --- front back, z --- up)
    data["vectors"][0] = np.array([[0, 1, 1], [1, 0, 1], [0, 0, 1]])
    data["vectors"][1] = np.array([[1, 0, 1], [0, 1, 1], [1, 1, 1]])
    # Front face
    data["vectors"][2] = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0]])
    data["vectors"][3] = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 0]])
    # Left face
    data["vectors"][4] = np.array([[0, 0, 0], [1, 0, 0], [1, 0, 1]])
    data["vectors"][5] = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 1]])
    # Bottom
    data["vectors"][6] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    data["vectors"][7] = np.array([[1, 0, 0], [0, 1, 0], [1, 1, 0]])
    # Back face
    data["vectors"][8] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    data["vectors"][9] = np.array([[0, 1, 1], [0, 0, 1], [0, 1, 0]])
    # Right face
    data["vectors"][10] = np.array([[0, 1, 1], [1, 1, 1], [1, 1, 0]])
    data["vectors"][11] = np.array([[0, 1, 1], [0, 1, 0], [1, 1, 0]])

    return data


def make_pyramid() -> ndarray:
    data = np.zeros(12, dtype=stl.mesh.Mesh.dtype)
    # Looks like everything is defined as a triangle
    # Top face
    # (x -- left right, y --- front back, z --- up)
    data["vectors"][0] = np.array([[-1, 1, 0], [1, 1, 0], [0, 0, 2]])
    data["vectors"][1] = np.array([[-1, 1, 0], [-1, -1, 0], [0, 0, 2]])
    data["vectors"][2] = np.array([[-1, -1, 0], [1, -1, 0], [0, 0, 2]])
    data["vectors"][3] = np.array([[1, -1, 0], [1, 1, 0], [0, 0, 2]])
    data["vectors"][4] = np.array([[-1, 1, 0], [1, 1, 0], [0, 0, 0]])
    data["vectors"][5] = np.array([[-1, 1, 0], [-1, -1, 0], [0, 0, 0]])
    data["vectors"][6] = np.array([[-1, -1, 0], [1, -1, 0], [0, 0, 0]])
    data["vectors"][7] = np.array([[1, -1, 0], [1, 1, 0], [0, 0, 0]])

    return data


def selection() -> int:
    return int(input("What model number do you choose? "))


def save_file() -> bool:
    save: str = input("Do you want to save your most recent model (y/n)? ")
    if save == "y".lower() or save == "yes".lower():
        return True
    else:
        return False


def initialize():
    # do the population thing
    # fitness will be an overarching thing, keeping track of which of the shapes
    # gets selected per generation so we can develop a tree
    global POPULATION
    global CURRENT_USER
    global CURRENT_DIRECTORY
    cube = make_cube()
    pyramid = make_pyramid()
    POPULATION = [cube, pyramid]
    CURRENT_USER = input("Input your Username: ")
    CURRENT_DIRECTORY = path_setup(CURRENT_USER)


def path_setup(username: str) -> str:
    cur_path: str = os.getcwd()
    path: str = cur_path + f"/Users/{username}/"
    path_to_make: List[str] = [""]
    for p in path_to_make:
        if not os.path.exists(os.path.join(path, p)):
            os.makedirs(os.path.join(path, p))
    return path


def generate_pop(selected: int) -> None:
    global POPULATION
    parent: ndarray = POPULATION[selected]
    new_pop: List[ndarray] = [deepcopy(parent) for _ in range(POP_SIZE)]
    for i in range(POP_SIZE):  # for the pop size
        if np.random.uniform(0, 1) < T_RATE:  # if not first evolution and we make new triangle
            t = np.random.randint(0, len(new_pop[i]["vectors"]))  # choose random triangle
            new_pop[i] = break_up_triangle(
                to_break=new_pop[i]["vectors"][t], index=t, parent=new_pop[i]
            )  # make more triangles
        if np.random.randint(0, 2) % 2 == 0:
            point_manipulation(new_pop[i], multiply_points)  # multiply a point by random value
        else:
            point_manipulation(new_pop[i], add_points)  # add a random value to a point
    POPULATION = new_pop


def point_manipulation(object: ndarray, manipulation) -> None:
    index = np.random.randint(len(object["vectors"]))
    point = object["vectors"][index][random.randint(0, 2)]
    compare = deepcopy(point)
    new_point = manipulation(point)
    for i in range(len(object["vectors"])):
        for j in range(len(object["vectors"][i])):
            if list(object["vectors"][i][j]) == list(compare):
                object["vectors"][i][j] = new_point


def multiply_points(point) -> None:
    if random.randint(0, 1) == 0:
        point *= random.uniform(0.1, 2)
    else:
        point *= random.uniform(-2, -0.1)
    return point


def add_points(point: ndarray) -> ndarray:
    largest: int = max(np.max(point[0]), np.max(point[1]), np.max(point[2]))
    point[0] += int(random.uniform(np.negative(largest / 2), largest / 2))
    point[1] += int(random.uniform(np.negative(largest / 2), largest / 2))
    point[2] += int(random.uniform(np.negative(largest / 2), largest / 2))
    return point


def midpoint(coords: ndarray) -> ndarray:
    final_list: List[List[float]] = []
    for i in range(coords.shape[0]):
        if i + 1 == coords.shape[0]:
            m_x = (coords[i][0] + coords[0][0]) / 2
            m_y = (coords[i][1] + coords[0][1]) / 2
            m_z = (coords[i][2] + coords[0][2]) / 2
            final_list.append([m_x, m_y, m_z])
        else:
            m_x = (coords[i][0] + coords[i + 1][0]) / 2
            m_y = (coords[i][1] + coords[i + 1][1]) / 2
            m_z = (coords[i][2] + coords[i + 1][2]) / 2
            final_list.append([m_x, m_y, m_z])
    return np.array(final_list)


def break_up_triangle(to_break: ndarray, index: int, parent: ndarray) -> ndarray:
    """
    Split a Mesh triangle into 4 identical ones
    :param to_break: a 3D numpy array of shape (3, 3), representing a triangle in 3D space
    """
    midpoints: ndarray = midpoint(to_break)
    # increase the size of the DATA object by 3 for the new sides we are adding
    new_data = np.zeros(parent.shape[0] + 3, dtype=stl.mesh.Mesh.dtype)
    for v in range(len(parent["vectors"])):
        new_data["vectors"][v] = deepcopy(parent["vectors"][v])
    new_data["vectors"][index] = np.array((midpoints[0], midpoints[1], midpoints[2]))
    new_data["vectors"][v + 1] = np.array([to_break[0], midpoints[0], midpoints[2]])
    new_data["vectors"][v + 2] = np.array([to_break[1], midpoints[0], midpoints[1]])
    new_data["vectors"][v + 3] = np.array([to_break[2], midpoints[1], midpoints[2]])
    return new_data


if __name__ == "__main__":
    # initialize population
    initialize()
    print(len(POPULATION))
    # make new pop
    generate_pop(0)
    for g in range(NUM_GEN):
        # show pop
        plot_population()
        # make new pop bases on selection
        selected: int = selection()
        # save?
        if save_file():
            save_and_plot(POPULATION[selected], f"{CURRENT_DIRECTORY}/final")
            break
        else:
            save_and_plot(POPULATION[selected], f"{CURRENT_DIRECTORY}/final_{g}")
        generate_pop(selected)
    print("Thanks :]")
