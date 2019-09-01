# encoding=utf8
# This is temporary fix to import module from parent folder
# It will be removed when package is published on PyPI
import sys
sys.path.append('../')
# End of fix

from NiaPy.algorithms.basic import DynamicFireworksAlgorithmGauss
from NiaPy.util import OptimizationType
from NiaPy.task.task import StoppingTask
from NiaPy.benchmarks import Sphere

# we will run Fireworks Algorithm for 5 independent runs
for i in range(5):
	task = StoppingTask(D=10, nGEN=50, optType=OptimizationType.MINIMIZATION, benchmark=Sphere())
	algo = DynamicFireworksAlgorithmGauss(N=70, Ainit=0.1, Afinal=0.9)
	best = algo.run(task=task)
	print('%s -> %s' % (best[0], best[1]))

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
