import os
import pytest
from OCCT.TopoDS import TopoDS_Shape
from declaracad.occ.plugin import load_model

@pytest.mark.skipif('TRAVIS' in os.environ, reason='Disabled for now')
@pytest.mark.parametrize('name', (
    'bearing',
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
    'vacuum_nozzle',
))
def test_example(qt_app, name):
    path = 'examples/%s.enaml' % name
    assembly = load_model(path)
    for shape in assembly:
        assert isinstance(shape.render(), TopoDS_Shape)
