@client.command()
async def play(ctx, *, song):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if ctx.author.voice is not None:  # Is the user in a channel?
        if voice is None:  # Is the bot in a channel?
            # Make the bot connect to channel and play the music

        else:  # The bot is in a channel:
            if ctx.guild.voice_client.channel == channel:  # Is the bot in the same channel as the user?
                # Stop the currently playing song and play new music

            else:  # No, he isn't
                # Give error

    else:  # User isn't connected to a channel!
        # Give error

@client.command()
async def pause(ctx):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice is not None: # Is the bot in a channel?
        if ctx.guild.voice_client.channel == channel: # Is the user in the same channel as the bot?
            if voice.is_playing(): # Is the bot even playing?
                # Simpy pause the voice

            else: # No he isn't playing
                # Give error

        else: # The user isn't in the same channel as the bot
            # give error

    else:  # Bot isn't in a channel
    # Give error

@client.command()
async def resume(ctx):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice is not None: # Is the bot in a channel?
        if ctx.guild.voice_client.channel == channel: # Is the user in the same channel as the bot?
            if voice.is_playing(): # Is the bot resumed?
                # Give error

            else: # Bot isn't resumed
                # Resume the bot

        else: # The user isn't in the same channel as the bot
            # Give error

    else:  # Bot isn't in a channel
    # Give error

@client.command()
async def leave(ctx):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice is not None: # Is the bot in a channel?
        if ctx.guild.voice_client.channel == channel: # Is the user in the same channel as the bot?
            # Disconnect the bot

        else: # Bot isn't in the same channel as the user
            # Give error

    else: # Bot isn't in a channel
        # Give error

@client.command()
async def stop(ctx):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if ctx.author.voice is not None: # Is the user in a channel?
        if voice is not None: # Is the bot in a channel?
            if ctx.guild.voice_client.channel == channel: # Are the user and the bot in the same channel?
                if voice.is_playing(): # Is the bot playing anything?
                    # Stop the bot

                else: # The bot isn't playing anything
                    # Give error

            else: # The user isn't in the same channel as the bot
                # Give error

        else: # The bot isn't connected to a channel
            # Give error

    else: # The user isn't connected to a channel
        # Give error