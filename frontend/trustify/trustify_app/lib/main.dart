import 'package:flutter/cupertino.dart';
import 'package:trustify_app/core/constants/app_constants.dart';
import 'package:trustify_app/core/theme/colors.dart';
import 'package:trustify_app/core/theme/theme.dart';
import 'package:trustify_app/features/verification/presentation/pages/verifier_page.dart';

void main() {
  runApp(const TrustifyApp());
}

class TrustifyApp extends StatelessWidget {
  const TrustifyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return CupertinoApp(
      debugShowCheckedModeBanner: false,
      title: AppConstants.appName,
      builder: _builder,
      home: VerifierPage(),
    );
  }
}

CupertinoTheme _builder(BuildContext context, Widget? child) {
  CupertinoThemeData theme = CupertinoTheme.of(context);
  final String fontFamily = AppTheme.fontFamily;
  theme = theme.copyWith(
    primaryColor: AppColors.primary,
    textTheme: theme.textTheme.copyWith(
      textStyle: theme.textTheme.textStyle.copyWith(fontFamily: fontFamily),
      navLargeTitleTextStyle: theme.textTheme.navLargeTitleTextStyle
          .copyWith(fontFamily: fontFamily),
      actionSmallTextStyle:
          theme.textTheme.actionSmallTextStyle.copyWith(fontFamily: fontFamily),
      actionTextStyle:
          theme.textTheme.actionTextStyle.copyWith(fontFamily: fontFamily),
      dateTimePickerTextStyle: theme.textTheme.dateTimePickerTextStyle
          .copyWith(fontFamily: fontFamily),
      navActionTextStyle:
          theme.textTheme.navActionTextStyle.copyWith(fontFamily: fontFamily),
      navTitleTextStyle:
          theme.textTheme.navTitleTextStyle.copyWith(fontFamily: fontFamily),
      pickerTextStyle:
          theme.textTheme.pickerTextStyle.copyWith(fontFamily: fontFamily),
      tabLabelTextStyle:
          theme.textTheme.tabLabelTextStyle.copyWith(fontFamily: fontFamily),
    ),
  );

  return CupertinoTheme(
    data: theme,
    child: DefaultTextStyle(
      style: theme.textTheme.textStyle.copyWith(
        fontFamily: fontFamily,
      ),
      child: child!,
    ),
  );
}
