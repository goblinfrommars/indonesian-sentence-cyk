import controller.cnf_conversion.cnf as cnf_cv

def get_grammar():
  dict = cnf_cv.run_conversion()
  return dict