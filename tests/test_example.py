from main import suma
def test_always_pass():
    assert True

def test_suma():
    result=suma(1,4)
    assert result == 5
    

