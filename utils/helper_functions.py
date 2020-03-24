import re
from typing import Union, Optional, List

import discord
from discord import Role


"""
####################################################################
########################## HELP FUNCTIONS ##########################
####################################################################
"""

def get_lab_group_name(number: int):
    return f"Group {number:2}"


def get_role_name(number: int):
    return f"member-group {number:2}"


def get_text_channel_name(number: int):
    return f"text-channel-{number}"


def get_voice_channel_name(number: int):
    return f"voice-channel {number}"


def get_lab_group(guild: discord.Guild, group: Union[int, str]) -> Optional[discord.CategoryChannel]:
    name = get_lab_group_name(group) if type(group) == int else group
    return discord.utils.get(guild.categories, name=name)


def get_lab_role(guild: discord.Guild, group: Union[int, str]) -> Optional[discord.Role]:
    name = get_role_name(group) if type(group) == int else group
    return discord.utils.get(guild.roles, name=name)


def get_lab_text_channel(guild: discord.Guild, group: Union[int, str]) -> Optional[discord.TextChannel]:
    name = get_text_channel_name(group) if type(group) == int else group
    return discord.utils.get(guild.channels, name=name)


def get_lab_voice_channel(guild: discord.Guild, group: Union[int, str]) -> Optional[discord.VoiceChannel]:
    name = get_voice_channel_name(group) if type(group) == int else group
    return discord.utils.get(guild.channels, name=name)


def all_existing_lab_roles(guild: discord.Guild) -> List[Role]:
    return list(filter(lambda r: re.search("member-group\s+[0-9]+", r.name), guild.roles))


def existing_group_number_from_role(role: discord.Role) -> Optional[int]:
    return int(re.sub("member-group\s+([0-9]+)", r"\1", role.name)) if re.search("member-group\s+[0-9]+", role.name) else None


def existing_group_number(member: discord.Member) -> Optional[int]:
    member_roles = member.roles
    for role in member_roles:
        group = existing_group_number_from_role(role)
        if group:
            return group
    return None


def existing_member_lab_role(member: discord.Member) -> Optional[Role]:
    member_roles = member.roles
    for role in member_roles:
        if re.search("member-group\s+[0-9]+", role.name):
            return role
    return None


def existing_member_lab_group(member: discord.Member) -> Optional[discord.CategoryChannel]:
    member_roles = member.roles
    for role in member_roles:
        if re.search("member-group\s+[0-9]+", role.name):
            num = int(re.sub("member-group\s+([0-9]+)", r"\1", role.name))
            return discord.utils.get(member.guild.categories, name=get_lab_group_name(num))
    return None


def existing_member_lab_text_channel(member: discord.Member) -> Optional[discord.TextChannel]:
    member_roles = member.roles
    for role in member_roles:
        if re.search("member-group\s+[0-9]+", role.name):
            num = int(re.sub("member-group\s+([0-9]+)", r"\1", role.name))
            return discord.utils.get(member.guild.channels, name=get_text_channel_name(num))
    return None


def existing_member_lab_voice_channel(member: discord.Member) -> Optional[discord.VoiceChannel]:
    member_roles = member.roles
    for role in member_roles:
        if re.search("member-group\s+[0-9]+", role.name):
            num = int(re.sub("member-group\s+([0-9]+)", r"\1", role.name))
            return discord.utils.get(member.guild.channels, name=get_voice_channel_name(num))
    return None