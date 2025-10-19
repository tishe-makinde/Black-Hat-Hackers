import 'package:file_picker/file_picker.dart';
import 'package:flutter/cupertino.dart';

class AddImageButton extends StatefulWidget {
  const AddImageButton({super.key});

  @override
  State<AddImageButton> createState() => _AddImageButtonState();
}

class _AddImageButtonState extends State<AddImageButton> {
  final double _containerDimension = 180.0;
  final BorderRadius _containerBorderRadius = BorderRadius.circular(8.0);
  final BorderRadius _buttonBorderRadius = BorderRadius.circular(30.0);
  PlatformFile? _image;

  @override
  Widget build(BuildContext context) {
    final CupertinoThemeData theme = CupertinoTheme.of(context);

    return Container(
      width: _containerDimension,
      height: _containerDimension,
      decoration: BoxDecoration(
        color: CupertinoColors.extraLightBackgroundGray,
        borderRadius: _containerBorderRadius,
        border: Border.all(color: CupertinoColors.lightBackgroundGray),
      ),
      child: _image == null
          ? Column(
              spacing: 2.0,
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                CupertinoButton.filled(
                  onPressed: () async {
                    FilePickerResult? result =
                        await FilePicker.platform.pickFiles();
                    if (result == null) {
                      return;
                    }
                    PlatformFile file = result.files.first;
                    setState(() {
                      _image = file;
                    });
                  },
                  padding: EdgeInsets.zero,
                  borderRadius: _buttonBorderRadius,
                  child: Icon(CupertinoIcons.camera_fill),
                ),
                Text(
                  'Add Image',
                  style: theme.textTheme.actionSmallTextStyle.copyWith(
                    color: CupertinoColors.darkBackgroundGray,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ],
            )
          : Padding(
              padding: const EdgeInsets.all(12.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    CupertinoIcons.photo_fill,
                    size: 50,
                  ),
                  SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Text(
                      _image!.name,
                      style: theme.textTheme.actionSmallTextStyle.copyWith(
                        color: CupertinoColors.darkBackgroundGray,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ),
                  CupertinoButton(
                    padding: EdgeInsets.zero,
                    onPressed: () {
                      setState(() {
                        _image = null;
                      });
                    },
                    child: Icon(
                      CupertinoIcons.delete,
                      color: CupertinoColors.systemRed,
                    ),
                  ),
                ],
              ),
            ),
    );
  }
}
