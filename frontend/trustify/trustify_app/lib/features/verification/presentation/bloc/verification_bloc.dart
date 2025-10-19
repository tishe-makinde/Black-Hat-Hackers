import 'package:dartz/dartz.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:trustify_app/core/error/failure.dart';
import 'package:trustify_app/features/verification/domain/usecases/verify_link_use_case.dart';
part 'verification_event.dart';
part 'verification_state.dart';

class VerificationBloc extends Bloc<VerificationEvent, VerificationState> {
  final VerifyLinkUseCase _verifyLink;
  VerificationBloc(
    VerifyLinkUseCase verifyLink,
  )   : _verifyLink = verifyLink,
        super(VerificationInitial()) {
    on<VerificationLink>((event, emit) async {
      final Either<Failure, Map<String, dynamic>> response =
          await _verifyLink(event.url);
      response.fold((l) => emit(VerificationFailure(l.message)),
          (r) => emit(LinkVerified(r)));
    });
  }
}
