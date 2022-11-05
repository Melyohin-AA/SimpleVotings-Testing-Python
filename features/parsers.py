import behave
import parse


@parse.with_pattern(r'"([^"]*)"')
def parse_text(text) -> str: return text[1:-1]


@parse.with_pattern(r"(\w*\/)+")
def parse_page(text) -> str: return text


@parse.with_pattern(r"[01]")
def parse_flag(text) -> bool: return text != '0'


behave.register_type(Text=parse_text, Page=parse_page, Flag=parse_flag)
behave.use_step_matcher("cfparse")
