# How To Use autorest.az to genreate entension code and try
## With Docker
1. Install [Docker](https://www.docker.com/products) if you haven't

2. Prepare following github repos:
   * Sync 'https://github.com/Azure/azure-cli-extensions.git' to {azure_cli_ext_folder}
   * Sync 'https://github.com/Azure/azure-rest-api-specs.git' to {swagger_folder}

3. Prepare specification config

   Make sure **readme.az.md**, **readme.cli.md** and **readme.python.md** is available in your swagger folder (like under {swagger_folder}/resource-manager/). If they are not there, you can refer to [configuration](https://github.com/Azure/autorest.az/tree/master/src/test/scenarios/attestation/configuration) as example

4. Login acr: **`az acr login --name amecodegen`**

5. Start docker: **`docker run -v {swagger_folder}:/home/swg -v {azure_cli_ext_folder}:/home/azext -v -it amecodegen.azurecr.io/az:2020.05.24 /bin/bash`**

   **Example**: `docker run -v d:\git\azure-rest-api-specs:/home/swg -v d:\git\azure-cli-extensions:/home/azext -it amecodegen.azurecr.io/az:2020.05.24 /bin/bash`

   **Tip**: The docker image version is decoupled from codegen version. As we release CodeGen version though NPM package which will be pulled by the docker image automatically, so in most case you won't need to pull a new docker image every time anymore.

6. Generate code:
   * Method 1: Alias `gen` can be used if you map your local folders to the ones in docker as above (/home/swg, /home/azext, /home/azcore): **`gen {service_name}`** The {service_name} is the folder name under azure-rest-api-specs/specification. 
   * Method 2: Otherwise, use: **`autorest --az --azure-cli-extension-folder=/home/azext  /home/swg/specification/{service_name}/resource-manager/readme.md`**

   **Tip**: --tag can be used to specify version, usually detail tag config can be found in {swagger_folder}/resource-manager/readme.md file

7. Try the generated extension
   * Through Azdev

     Now you should already be able to use your local azdev to try the generated extension, but you can also use the azdev installed in the docker if you want:
     1. **`activate`**
     2. **`azdev setup --cli /home/azcore --repo /home/azext --ext {service_name}`**
         * **Tip 1**: This may take ~5 minutes for the first time
         * **Tip 2**: alias `setup` is provided for 'azdev setup' if you map your local folders to the ones listed above. Example: `setup {service_name}`
         * **Tip 3**: alias `add` is provided for 'azdev extension add…' if you map your local folders to the ones listed above. Example: `add {service_name}`
     3. **`az {service_name}`**

   * Through Package

     You can also package generated code into a whl file directly for az to use with following step:
     1. (**in docker**) Run **`python setup.py sdist bdist_wheel`** in folder containing your generated code (/home/azext/src/{service_name}). The generated whl file can be found at /home/azext/src/{service_name}/dist
     2. (**in your host machine**) **`az extension add --source={path to the whl file}`** once make sure the latest azure-cli is installed.

        **Example**: `az extension add --source=.\aisc-0.1.0-py3-none-any.whl`

8. Run CLI tests in azdev: **`azdev test {service_name}`**
 
## From Swagger Pipeline 
We are integrating Azure CLI CodeGen with the swagger pipeline now so that you can get the generated code and package directly without running the command. It's coming soon. Please stay tuned. :)

# Support & Doc
## Issue Report
* For any issue found, please file issue at [Github](https://github.com/Azure/autorest.az/issues), Please also file issue to us if you find some doc is missing or more detail is needed.
* Please use [AME CodeGen Teams Channel](https://teams.microsoft.com/l/channel/19%3a031673a5362e4ff18bd7886a4ac7798a%40thread.skype/CodeGen?groupId=de995b1a-16c1-4cc7-a49b-bc9f90bc6acd&tenantId=72f988bf-86f1-41af-91ab-2d7cd011db47) for quick support and questions.
## Document
* Document is updated to github at [FAQ](https://github.com/Azure/autorest.az/blob/master/doc/faq.md)
