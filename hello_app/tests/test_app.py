# this file is needed for the Azure Pipeline build to pass. 
# Otherwise pyTest fails the build with exit code "5", 
# which means it found no files in the project that start with "test_". 

# dummy function
def func(a):
    return a-1

def test_testmethod():
    assert func(6) == 5