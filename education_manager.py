{formatted_subjects}```")
                await ctx.send(embed=embed)
                return

            subject = subject.lower()
            if subject not in self.chapters[11]:
                await ctx.send(f"❌ Invalid subject. Available subjects: {', '.join(self.chapters[11].keys())}")
                return

            embed = discord.Embed(
                title=f"📖 Class 11 {subject.title()} Chapters",
                color=discord.Color.green()
            )

            chapter_list = self.chapters[11][subject]
            formatted_chapters = "\n".join([f"{i+1}. {chapter}" for i, chapter in enumerate(chapter_list)])

            embed.add_field(
                name="Chapters",
                value=f"```{formatted_chapters}```",
                inline=False
            )

            embed.set_footer(text=f"Use !11 {subject} <chapter_name> to get questions!")
            await ctx.send(embed=embed)

        except Exception as e:
            self.logger.error(f"Error in view_chapters_11: {e}")
            await ctx.send("❌ An error occurred while fetching chapters. Please try again.")

    @commands.command(name='chapters12')
    async def view_chapters_12(self, ctx, subject: str = None):
        """View chapters for Class 12 subjects"""
        try:
            if not subject:
                embed = discord.Embed(
                    title="📚 Available Subjects for Class 12",
                    description="Please specify a subject: !chapters12 <subject>",
                    color=discord.Color.blue()
                )
                subjects = list(self.chapters[12].keys())
                formatted_subjects = "\n".join([f"• {subj.title()}" for subj in subjects])
                embed.add_field(name="Subjects:", value=f"```{formatted_subjects}```")
                await ctx.send(embed=embed)
                return

            subject = subject.lower()
            if subject not in self.chapters[12]:
                await ctx.send(f"❌ Invalid subject. Available subjects: {', '.join(self.chapters[12].keys())}")
                return

            embed = discord.Embed(
                title=f"📖 Class 12 {subject.title()} Chapters",
                color=discord.Color.green()
            )

            chapter_list = self.chapters[12][subject]
            formatted_chapters = "\n".join([f"{i+1}. {chapter}" for i, chapter in enumerate(chapter_list)])

            embed.add_field(
                name="Chapters",
                value=f"```{formatted_chapters}```",
                inline=False
            )

            embed.set_footer(text=f"Use !12 {subject} <chapter_name> to get questions!")
            await ctx.send(embed=embed)

        except Exception as e:
            self.logger.error(f"Error in view_chapters_12: {e}")
            await ctx.send("❌ An error occurred while fetching chapters. Please try again.")

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Check bot's latency"""
        latency = round(self.bot.latency * 1000)
        ping_embed = discord.Embed(
            title="🏓 Pong!",
            description=f"Bot latency: {latency}ms",
            color=discord.Color.green() if latency < 200 else discord.Color.orange()
        )

        if latency < 100:
            status = "🟢 Excellent"
        elif latency < 200:
            status = "🟡 Good"
        else:
            status = "🔴 Poor"

        ping_embed.add_field(
            name="Connection Quality",
            value=status,
            inline=False
        )
        await ctx.send(embed=ping_embed)

    @commands.command(name='help')
    async def help_command(self, ctx):
        """Show help information with fancy formatting"""
        help_embed = discord.Embed(
            title="📚 Educational Bot Help",
            description="Your personal study companion for Class 11 & 12!",
            color=discord.Color.blue()
        )

        # Main Commands Section
        commands_info = (
            "```ansi\n"
            "[1;34m┏━━━━━ Main Commands ━━━━━┓[0m\n"
            "[1;32m!11[0m - Get Class 11 Questions\n"
            "[1;32m!12[0m - Get Class 12 Questions\n"
            "[1;32m!subjects[0m - List All Subjects\n"
            "[1;32m!chapters11[0m - View Class 11 Chapters\n"
            "[1;32m!chapters12[0m - View Class 12 Chapters\n"
            "[1;32m!ping[0m - Check Bot Status\n"
            "[1;32m!refresh[0m - Reload Bot (Admin)\n"
            "[1;34m┗━━━━━━━━━━━━━━━━━━━━━━━┛[0m\n"
            "