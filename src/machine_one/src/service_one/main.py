help("modules")
import common_project

if __name__ == "__main__":
    print(dir(common_project))
    import pdb; pdb.set_trace()

    #print(dir(common_project.common_project))
    #print(dir(common_project.common_project.common_project))
    try:
        common_project.common_func()
    except AttributeError:
        common_project.common_project.common_func()
