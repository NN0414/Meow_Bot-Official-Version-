import discord
from discord.ext import commands
from core.classes import Cog_Extension
import re


class easycalc(Cog_Extension):
    def __init__(self,ctx):
        self.legal = re.compile(r'^[\.\de\+\-\*/% \(\)]*$')
        symbol_list = ['[\d]+e[\+\-][\d]+', '[\d\.]+', '\+', '\-', '\*', '/', '%', '\(', '\)']
        self.symbol = re.compile('(%s)' % '|'.join(symbol_list))
    @commands.command()
    async def calc(self,ctx,expr):
      try:
        self._is_easy(expr)
        self._no_exp(expr)
        self._is_calculable(expr)
        await ctx.send('計算結果：%s = %s' % (self._pretty_expr(expr), str(eval(expr)).upper()))
      except Exception as e:
        await ctx.send(str(e))

    def _pretty_expr(self, expr):
        result = self.symbol.findall(expr)
        return ' '.join(result).replace('( ', '(').replace(' )', ')')

    def _is_easy(self, expr):
        if self.legal.match(expr) is None:
            raise easycalc.NotEasyExpression()
        return True

    def _no_exp(self, expr):
        if '**' in expr:
            raise easycalc.ExponentNotAllowed()
        return True

    def _is_calculable(self, expr):
        try:
            exec(expr)
            return True
        except ZeroDivisionError:
            raise easycalc.DividByZero()
        except:easycalc.NotCalculable()

    class NotEasyExpression(Exception):
        def __str__(self):
            return '只能包含數字和 + - * / %'

    class ExponentNotAllowed(Exception):
        def __str__(self):
            return '不支援指數運算'

    class NotCalculable(Exception):
        def __str__(self):
            return '運算式格是錯誤'

    class DividByZero(Exception):
        def __str__(self):
            return '算式出現除以零的錯誤'


def setup(bot):
  bot.add_cog(easycalc(bot))