from BayesNet import BayesNet
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

bifxml_path = "testing/lecture_example2.BIFXML"

bn = BayesNet()
bn.load_from_bifxml(bifxml_path)
bn.draw_structure()