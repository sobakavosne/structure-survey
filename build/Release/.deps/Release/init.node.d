cmd_Release/init.node := ln -f "Release/obj.target/init.node" "Release/init.node" 2>/dev/null || (rm -rf "Release/init.node" && cp -af "Release/obj.target/init.node" "Release/init.node")
