from glimps_custom_modules import GlimpsCustomModule

from glimps_custom_modules.action_youpi import Youpi


if __name__ == "__main__":
    module = GlimpsCustomModule()
    module.register(Youpi, "Youpi")
    module.run()
