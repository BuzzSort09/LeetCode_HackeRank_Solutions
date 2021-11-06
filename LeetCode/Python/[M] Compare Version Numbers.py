class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        # O(n)
        # split version with '.'
        first_version = [int(ver) for ver in version1.split('.')]
        second_version = [int(ver) for ver in version2.split('.')]
        
        # O(n)
        for index in range(0, max(len(first_version), len(second_version))):
            # read version from first_version list
            if index >= len(first_version):
                ver1 = 0
            else:
                ver1 = first_version[index]
                
            # read version from second_version list
            if index >= len(second_version):
                ver2 = 0
            else:
                ver2 = second_version[index]
            
            # compare the versions
            if ver1 > ver2:
                return 1
            elif ver1 < ver2:
                return -1
                
        return 0