from .core import RoleManagement


async def setup(bot):
    cog = RoleManagement(bot)
    await bot.add_cog(cog)
    cog.init()
