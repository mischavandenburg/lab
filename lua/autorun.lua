--- :echo nvim_get_current_buf()
-- https://www.youtube.com/watch?v=9gUatBHuXE0

local bufnr = 5

-- this writes hello world to the selected buffer
-- whenver the buffer is run with :source %
-- the -1 means the index past the end of the file
-- vim.api.nvim_buf_set_lines(bufnr, 0, -1, false, { "hello", "world" })


-- a function that runs every time we save a file
vim.api.nvim_create_autocmd("BufWritePost", {
	-- the group makes sure we don't keep adding autocommands every time we save the file
	group = vim.api.nvim_create_augroup("Mischas Group", { clear = true }),
	pattern = "*.py",
	callback = function()
		-- print("wow we saved a file")
		-- 0, 0 means start 0 end 0, so the beginning of the file
		-- the 0th spot
		vim.api.nvim_buf_set_lines(bufnr, 0, -1, false, { "hello", "world!" })
		vim.fn.jobstart({ "python", "hello.py" }, {
			-- stdout buffered means "please only send
			-- full lines", "send me the out put 1 line at a time"
			stdout_buffered = true,
			-- whenever we get a stdout message:
			on_stdout = function(_, data)
				-- if we have data, it could be nil so we need to catch that
				if data then
					-- at the very end of the file, append data
					vim.api.nvim_buf_set_lines(bufnr, -1, -1, false, data)
				end
			end,
			})
	end,
})
