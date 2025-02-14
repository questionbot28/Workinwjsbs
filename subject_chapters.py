{chapter_text}```",
            inline=False
        )

        embed.set_footer(text=f"Use !11 {subject} <chapter_name> to get questions!")
        await ctx.send(embed=embed)

    @commands.command(name='viewchapters12')
    async def view_chapters_12(self, ctx, subject: str):
        """View chapters for class 12 subjects"""
        subject = subject.lower()
        if subject not in self.subjects_data:
            available_subjects = list(self.subjects_data.keys())
            await ctx.send(f"❌ Invalid subject. Available subjects: {', '.join(available_subjects)}")
            return

        chapters = self.subjects_data[subject][12]
        embed = discord.Embed(
            title=f"📚 {subject.title()} - Class 12",
            description="Here are the chapters for your selected subject:",
            color=discord.Color.blue()
        )

        chapter_text = "\n".join([f"{i+1}. {chapter}" for i, chapter in enumerate(chapters)])
        embed.add_field(
            name="Chapters",
            value=f"```{chapter_text}