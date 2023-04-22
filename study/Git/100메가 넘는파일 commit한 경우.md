#  GH001: Large files detected. 에러
### push한 파일 중 100mb가 넘는 파일이 존재할 경우 발생하는 에러
- 에러메시지
    ``` 
    remote: error: Trace: 068907a72faae7ac773059b0fc1d846fe962699c0856786967676c8d3afb3910
    remote: error: See http://git.io/iEPt8g for more information.
    remote: error: File assets/external_files/open_pose/pose_iter_160000.caffemodel is 196.41 MB; this exceeds GitHub's file size limit of 100.00 M 
    remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
    ```
- 이 경우 단순히 해당 파일을 삭제하고 다시 커밋하는 걸로 해결하지 못한다.
- 해당 파일을 push했던 commit 내역을 지워주어야 한다.
- 이 때, reset으로 해결하지 못하며 직접 파일 경로를 입력하여 제거해주어야한다.
    ``` 
    git filter-branch --tree-filter 'rm -rf  100/메가/넘는/파일의경로/파일명
    ```