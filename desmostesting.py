import DesmosKiller.main as main
def func(x):
    return (2*(x**2)) + (5*x) + 5

main.generate_array_then_graph(-100,100,func,1)
main.show()