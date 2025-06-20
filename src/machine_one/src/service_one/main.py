#help("modules")
import common_project

if __name__ == "__main__":
    print(dir(common_project))
#    import pdb; pdb.set_trace()

    #print(dir(common_project.common_project))
    #print(dir(common_project.common_project.common_project))
    common_project.common_project_func.common_func()
