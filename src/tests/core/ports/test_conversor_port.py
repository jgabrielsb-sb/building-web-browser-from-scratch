import pytest
from building_web_browser_from_scratch.core.ports.conversor_port import Conversor
from building_web_browser_from_scratch.core.exceptions import ConversorPortException


def test_class_without_run_implementation_raises_exception():
    """Test that a class without _run implementation raises TypeError when instantiated."""
    class IncompleteConversor(Conversor):
        pass
    
    with pytest.raises(TypeError, match="Can't instantiate abstract class"):
        IncompleteConversor()


def test_run_raises_conversor_port_exception_when_run_raises_exception():
    """Test that any exception raised by _run makes run raise ConversorPortException."""
    
    class FailingConversor(Conversor):
        def _run(self, input: any) -> any:
            raise ValueError("Test error")
    
    conversor = FailingConversor()
    
    with pytest.raises(ConversorPortException) as exception:
        conversor.run("test_input")

    assert "Error on conversor" in str(exception)

