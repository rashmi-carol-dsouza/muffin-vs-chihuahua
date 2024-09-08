Steps to Create and Activate a Virtual Environment:

1. Create the Virtual Environment
Run this command in your terminal or command prompt:

```
python3 -m venv myenv
```
myenv: This is the name of the virtual environment. You can replace it with any name you prefer.

2. Activate the Virtual Environment
Once the environment is created, you can activate it. The activation command depends on your operating system.

On macOS/Linux:

```
source myenv/bin/activate
```

On Windows (CMD):
```
myenv\Scripts\activate
```

On Windows (PowerShell):
```
.\myenv\Scripts\Activate
```
3. Deactivate the Virtual Environment

To deactivate the virtual environment when you're done working, use the following command:

```
deactivate
```