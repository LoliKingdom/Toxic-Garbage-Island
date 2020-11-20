import glob, zipfile, json

def get_mcmod_info_ids():
    mods = dict()
    jars = [file for file in glob.glob("mods/**/*.jar", recursive=True)]
    for num, jar in enumerate(jars):
        print(num, ": ", jar, sep="")
        opened_jar = zipfile.ZipFile(jar, 'r')
        try:
            jar_files = opened_jar.infolist()
            for jar_file in jar_files:
                if jar_file.filename.endswith('.info'):
                    try:
                        mcmod_info_file = opened_jar.open(jar_file)
                        mcmod_info = json.load(mcmod_info_file, strict=False)
                        for obj in mcmod_info:
                            try:
                                mod_name = obj["name"]
                                if examine_stupidness(jar, mod_name):
                                    mods[mod_name[0].capitalize() + mod_name[1:]] = jar.split("\\")[-1]
                            except (TypeError, KeyError):
                                if type(obj) is str:
                                    if type(mcmod_info[obj]) is list:
                                        mod_name = mcmod_info[obj][0]["name"]
                                        if examine_stupidness(jar, mod_name):
                                            mods[mod_name[0].capitalize() + mod_name[1:]] = jar.split("\\")[-1]
                                else:
                                    print("Something went wrong for:", jar)
                    except (json.decoder.JSONDecodeError, UnicodeDecodeError):
                        name = ""
                        split_jar_name = jar.split("\\")[-1]
                        for char in split_jar_name:
                            if char.isspace() or char.isalpha():
                                name = name + char
                            else:
                                break
                        mods[name] = split_jar_name
        finally:
            opened_jar.close()
    return mods

def examine_stupidness(jar, mod_name):
    if mod_name == "Example Mod":
        print(jar, "has an Example Mod mcmod.info left-over!")
        return False
    return True

file = open('modlist.txt', 'w')
for mod, jar in sorted(get_mcmod_info_ids().items()):
    file.write(mod + ", " + jar)
    file.write('\n')
file.close()

