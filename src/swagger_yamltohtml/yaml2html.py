import yaml, json, sys, os

MODULE_NAME = "swagger_yaml_to_html"
DIR_PATH = os.path.dirname(os.path.realpath(__file__))

def getArgvFlags(argv, flag_name, all_flags, base_url, bad_return=None):
  if flag_name in argv:
    index = argv.index(flag_name)
    if len(argv) > index+1:
      if argv[index+1] not in all_flags:
        return f"{base_url}/{argv[index+1]}"
  return bad_return

def convertYamlInHtml(base_path):
  all_flags = ['--yaml-file', '--html-file']
  if len(sys.argv) != 0:
    yaml_path = getArgvFlags(sys.argv, '--yaml-file', all_flags, base_path)
    html_path = getArgvFlags(sys.argv, '--html-file', all_flags, base_path, f'{DIR_PATH}/static/swagger.html')
    if yaml_path != None:
      spec = {}
      try:
        spec = yaml.safe_load(open(yaml_path, 'r'))
      except yaml.YAMLError as e:
        print(str(e))
        return False
    else:
      print("\nInput YAML Mode\nOn Linux: [Ctrl+d twice to leave]\nOn Windows: [Ctrl+z and enter key twice to leave]]\n")
      spec = yaml.load(sys.stdin, Loader=yaml.FullLoader)
    
    try:
      with open(html_path, 'r') as file:
        template = file.read()
    except Exception as e:
      print(f"HTML FILE ERROR: {str(e)}")
      return False
  
  print("\nConversion Succeded! \n")
  return (template % json.dumps(spec))
