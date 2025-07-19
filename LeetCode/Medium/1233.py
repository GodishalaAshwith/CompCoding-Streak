class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        res = []
        folder.sort()

        prev = ""
        for f in folder:
            if not prev or not f.startswith(prev + '/'):
                res.append(f)
                prev = f

        return res
