import pytest
from OCCT.TopoDS import TopoDS_Shape
from declaracad.occ.plugin import load_model

@pytest.mark.parametrize('name', (
    'bolt',
    'bottle',
    'chamfers',
    'dahlgren300z',
    'draw',
    'exhaust_flange',
    'faces',
    'fillets',
    'gcode',
    'half_space',
    #'house',
    'load',
    #'nemastepper',
    'operations',
    'pipes',
    'raw_shape',
    #'rib',
    'shapes',
    'spring',
    'svg',
    'sweeps',
    'threads',
    'thru_sections',
    'turners_cube',
))
def test_example(qt_app, name):
    path = 'examples/%s.enaml' % name
    assembly = load_model(path)
    for shape in assembly:
        assert isinstance(shape.render(), TopoDS_Shape)