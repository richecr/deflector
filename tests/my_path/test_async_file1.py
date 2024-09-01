import asyncio

from sentinel.helpers.after_each import after_each
from sentinel.helpers.before_each import before_each
from sentinel.helpers.describe import describe
from sentinel.helpers.it import it
from sentinel.modules.essentials.ensure import ensure


async def main() -> int:
    await asyncio.sleep(1)
    return 2


@describe("Main 1")
def describe_main() -> None:
    x = 1

    @before_each()
    async def start() -> bool:
        nonlocal x
        await asyncio.sleep(1)
        x += 1
        return True

    @after_each()
    async def end_() -> bool:
        nonlocal x
        await asyncio.sleep(1)
        x = 1
        return True

    @it("It Test 1")
    async def test1() -> None:
        v = await main()
        ensure.equal(x, 2, "Equal Before Each")
        ensure.equal(v, 2, "Equal 1")
        ensure.equal(v, 2, "Equal 2")

    @it("It Test 2")
    async def test2() -> None:
        v = await main()
        ensure.equal(x, 2, "Equal After Each")
        ensure.equal(v, 2, "Equal")
        ensure.not_equal(v, 1, "Not Equal")
        ensure.ok(True, "Ok")
        ensure.match_re("acab", "ab", "Match Re")
        ensure.does_not_match_re("a", "ab", "Does Not Match Re")


ensure.equal(1, 1, "Ops")
