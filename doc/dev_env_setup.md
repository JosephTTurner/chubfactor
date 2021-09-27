# Setup Notes

[TOC]

## WSL2 and MySQL

There is some wierdness in how WSL2 handles localhost/127.0.0.1/etc. Basically WSL2 creates it's own separate understood network addresses for itself and the native Windows host. So it's necessary to make a few adjustments to your set up that you wouldn't have to with WSL1.

Hopefully WSL2 will be updated to play more nicely with the Windows Host.

1. Install WSL2 on compatible Windows machine.
    - I used Ubuntu 20.04 as my hosted OS
    - Install Windows Terminal and set WSL2 as your default
2. Install git on WSL2 instance.
3. Install MySQL on Windows machine.

    - Use MySQL community installer to install
        - MySQL Server
        - MySQL WorkBench
        - MySQL Connector Python
    - Everything you need is covered if you select the developer default installation.
    - Make sure you allow the install wizard to start the MySQL service for you.

4. Add root user account for WSL2 instance.

    - Open MySQL Workbench
    - Start a new query if there is not already a query editor
    - Copy and paste the following commands into the MySQL server and click the lightnight bolt to run them both - or ctrl + enter with both commands selected.
    ```sql
    CREATE USER 'root'@'172.0.0.0/255.0.0.0' IDENTIFIED BY 'st@ychubb33';
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'172.0.0.0/255.0.0.0' WITH GRANT OPTION;
    ```
    - Using the range `172.0.0.0/225.0.0.0` covers potential changes to local IP address changes on rebooting / reconnecting to your network.
    - You might not want to do this on an untrusted network.

5. Export your host IP in WSL2 .bashrc
    - Add the following line to ~/.bashrc
    -   ```bash
        export WSL_HOST_IP=$(awk '/nameserver/ { print $2 }' /etc/resolv.conf)
        ```
    - You can later use this environment variable as the target IP address for a connection to a database hosted on your native windows machine MySQL Service

6. For more consistent connectivity / networking
    - (Follow these instructions)[https://github.com/microsoft/WSL/issues/4150#issuecomment-504209723]

## VS Code

VS Code plays much more nicely with python (and perhaps all) programming platforms when you have all the right plugins and workspace settings enabled. I reccomend allowing VS Code to install plugins that it claims would be helpful, but use your judgement and research options that might work best for you.

At time of writing I have enabled the following plugins:

Local - Installed:

 - Remote - WSL
    - Globally enabled
 - Better Jinja
 - DotENV
 - kconfig
 - Jinja
 - HTML BoilerPlate
 - HTML Snippets
 - JSPrintManager
 - PythonExtended
 - python snippets

WSL: Ubuntu-20.04 - Installed

 - Python
 - Pylnce
 - Visual Studio Intellicode
 - Close HTML/XML tag
 - EditorConfig for VS Code
 - JS-CSS-HTML Formatter
 - IntelliSense for CSS class names
 - Jupyter
    - Not sure it's used much

Next you want to define settings for some of these packages because the defaults don't cover your use cases, or because adjustments need to be made for them to work together nicely.

I guess one can just check the *.code-workspace file but here is what it looked like at time of writing:

```json
{
	"folders": [
		{
			"path": "."
		},
	],
	"settings": {
		"python.testing.pytestArgs": [
        	"app"
    	],
		"python.testing.unittestEnabled": false,
		"python.testing.pytestEnabled": true,
		"python.defaultInterpreterPath": "venv/bin/python",
		"python.analysis.autoImportCompletions": true,
		"files.associations": {
			"*.html": "jinja-html",
			"*.j2": "jinja-html",
			"*.shtml": "jinja-html"
		},
        "html.autoClosingTags": true,
        "emmet.includeLanguages": { "jinja-html": "html" },
        "editor.defaultFormatter": "vscode.emmet",
		"python.analysis.extraPaths": [
			"app"
		],
		"python.autoComplete.extraPaths": [
			"app"
		],
		"editor.trimAutoWhitespace": false,
		"[python]": {
			"editor.defaultFormatter": "ms-python.python"
		},
		"remote.SSH.remoteServerListenOnSocket": true,
	}
}
```

## Edit Remote Code on Raspberry Pi via VS Code SSH (optional but fun)
I followed [these instructions](https://code.visualstudio.com/docs/remote/troubleshooting) to create the necessary keys and connections to open the code located on my rasperry pi without entering a password everytime.

Where it says this in your ssh config file...
```config
Host name-of-ssh-host-here
    User your-user-name-on-host
    HostName host-fqdn-or-ip-goes-here
    IdentityFile ~/.ssh/id_rsa-remote-ssh
```
I was confused by the "~" for some reason also pointing to my Windows User directory. I just copied the identity file over to `C:\\Users\<user name>\.ssh` and it worked.
