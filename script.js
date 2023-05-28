const { execSync } = require("child_process");

for (var i = 2; i <= 10; i++) {
	execSync(`touch hw2-${i}.py`);
}
