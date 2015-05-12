FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/nahchoina/msg"
  "../src/nahchoina/srv"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "../src/nahchoina/srv/__init__.py"
  "../src/nahchoina/srv/_BumpData.py"
  "../src/nahchoina/srv/_CliffData.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
