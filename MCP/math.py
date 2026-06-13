from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add_numbers(a:int, b:int )->int:
    """
     Add two number's
     arges:
     a : 
     b:

     add the two number numbers
    """
    return a+b

if __name__ =="__main__":
    mcp.run(transport="stdio")