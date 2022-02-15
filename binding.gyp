{
  "targets": [
    {
      "target_name": "init",
	    "include_dirs": ["<!@(node -p \"require('node-addon-api').include\")"],
	    "dependencies": ["<!(node -p \"require('node-addon-api').gyp\")"],
      "defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ],
      "sources": [ "source/cpp-addon/addon.cpp" ]
    }
  ]
}