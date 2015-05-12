FILE(REMOVE_RECURSE
  "../msg_gen"
  "../srv_gen"
  "../msg_gen"
  "../srv_gen"
  "../src/nahchoina/msg"
  "../src/nahchoina/srv"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "../srv_gen/lisp/BumpData.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_BumpData.lisp"
  "../srv_gen/lisp/CliffData.lisp"
  "../srv_gen/lisp/_package.lisp"
  "../srv_gen/lisp/_package_CliffData.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
